from django import forms
from django.contrib import admin
from hotel.models import  ICON_CHOICES,Hotel, Room, Booking, RoomServices, HotelGallery, RoomTypeGallery,RoomTypeFeatures, HotelFeatures, HotelFAQs, RoomType, RoomTypeDescription,ActivityLog, StaffOnDuty, Coupon, CouponUsers, Notification, Bookmark, Review
from import_export.admin import ImportExportModelAdmin

from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .widgets import IconSelectWidget

class HotelAdminForm(forms.ModelForm):
    description_ru = forms.CharField(widget=CKEditorUploadingWidget())
    description_kk = forms.CharField(widget=CKEditorUploadingWidget())
    description_en = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Hotel
        fields = '__all__'

class HotelFeaturesForm(forms.ModelForm):
    class Meta:
        model = HotelFeatures
        fields = '__all__'
        widgets = {
            'icon': IconSelectWidget(choices=ICON_CHOICES)  # Используем кастомный виджет
        }


class RoomTypeFeaturesForm(forms.ModelForm):
    class Meta:
        model = RoomTypeFeatures
        fields = '__all__'
        widgets = {
            'icon': IconSelectWidget(choices=ICON_CHOICES)  # Используем кастомный виджет для поля icon
        }

class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = '__all__'   

class RoomTypeDescriptionForm(forms.ModelForm):
    description_ru = forms.CharField(widget=CKEditorUploadingWidget(attrs={'cols': 100, 'rows': 100}))
    description_kk = forms.CharField(widget=CKEditorUploadingWidget())
    description_en = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = RoomTypeDescription
        fields = '__all__'
        
    class Media:
        css = {
            'all': ('css/custom_admin.css',),  # Подключаем кастомный CSS
        }
class HotelGallery_Tab(admin.TabularInline):
    model = HotelGallery
    extra = 0


class HotelFeatures_Tab(admin.TabularInline):
    model = HotelFeatures
    form = HotelFeaturesForm  # Подключаем кастомную форму с виджетом
    extra = 0

class HotelFAQs_Tab(admin.TabularInline):
    model = HotelFAQs
    exclude = ['question', 'answer']
    extra = 0

class Room_Tab(admin.TabularInline):
    model = Room
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "room_type":
            parent_id = request.resolver_match.kwargs.get('object_id')  # Получаем ID текущего отеля
            if parent_id:
                kwargs["queryset"] = RoomType.objects.filter(hotel_id=parent_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class RoomTypeDescription_Tab(admin.TabularInline):
    model = RoomTypeDescription
    form = RoomTypeDescriptionForm
    extra = 0
    exclude = ['description']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "room_type":
            parent_id = request.resolver_match.kwargs.get('object_id')  # Получаем ID текущего отеля
            if parent_id:
                kwargs["queryset"] = RoomType.objects.filter(hotel_id=parent_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class ActivityLog_Tab(admin.TabularInline):
    model = ActivityLog

class StaffOnDuty_Tab(admin.TabularInline):
    model = StaffOnDuty

class CouponUsers_Tab(admin.TabularInline):
    model = CouponUsers



class RoomType_Tab(admin.TabularInline):
    model = RoomType
    form = RoomTypeForm
    #exclude = ['room_description']
    extra = 0

class RoomTypeGallery_Tab(admin.TabularInline):
    model = RoomTypeGallery
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "room_type":
            parent_id = request.resolver_match.kwargs.get('object_id')  # Получаем ID текущего отеля
            if parent_id:
                kwargs["queryset"] = RoomType.objects.filter(hotel_id=parent_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class RoomTypeFeatures_Tab(admin.TabularInline):
    model = RoomTypeFeatures
    form = RoomTypeFeaturesForm
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "room_type":
            parent_id = request.resolver_match.kwargs.get('object_id')  # Получаем ID текущего отеля
            if parent_id:
                kwargs["queryset"] = RoomType.objects.filter(hotel_id=parent_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)





class HotelAdmin(ImportExportModelAdmin):
    form = HotelAdminForm
    inlines = [HotelGallery_Tab, HotelFeatures_Tab, RoomType_Tab, RoomTypeDescription_Tab,RoomTypeGallery_Tab, RoomTypeFeatures_Tab, Room_Tab, HotelFAQs_Tab]
    search_fields = ['user__username', 'name']  
    list_filter = ['featured', 'status']
    list_editable = ['status']
    list_display = ['thumbnail', 'user', 'status', 'featured', 'views']  # Убираем 'name' из отображаемых полей
    list_per_page = 100
    prepopulated_fields = {"slug": ("name", )}
    exclude = ['description']  # Поле 'description' можно исключить как обычно

    # Переопределяем метод get_form для скрытия поля 'name' из формы редактирования
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if 'name' in form.base_fields:
            form.base_fields['name'].widget = forms.HiddenInput()  # Скрываем поле 'name'
        return form

class RoomAdmin(ImportExportModelAdmin):
    list_display = ['hotel' ,'room_number',  'room_type', 'price', 'number_of_beds' ,'is_available']
    list_per_page = 100


class BookingAdmin(ImportExportModelAdmin):
    inlines = [ActivityLog_Tab, StaffOnDuty_Tab]
    list_filter = [ 'hotel', 'room_type', 'check_in_date', 'check_out_date', 'is_active' , 'checked_in' ,'checked_out']
    list_display = ['booking_id', 'user', 'hotel', 'room_type', 'rooms', 'total', 'total_days', 'num_adults', 'num_children', 'check_in_date', 'check_out_date', 'is_active' , 'checked_in' ,'checked_out']
    search_fields = ['booking_id', 'user__username', 'user__email']
    list_per_page = 100


class RoomServicesAdmin(ImportExportModelAdmin):
    list_display = ['booking' ,'room', 'date', 'price', 'service_type']
    list_per_page = 100

class CouponAdmin(ImportExportModelAdmin):
    inlines = [CouponUsers_Tab]
    list_editable = ['valid_from', 'valid_to', 'active', 'type']
    list_display = ['code', 'discount', 'type', 'redemption', 'valid_from', 'valid_to' , 'active', 'date']
        
class NotificationAdmin(ImportExportModelAdmin):
    list_editable = ['seen', 'type']
    list_display = ['user', 'booking', 'type', 'seen', 'date']

class BookmarkAdmin(ImportExportModelAdmin):
    list_display = ['user', 'hotel']

class ReviewAdmin(admin.ModelAdmin):
    list_editable = ['active']
    list_display = ['user', 'hotel', 'review', 'reply' ,'rating', 'active']


admin.site.register(Hotel, HotelAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(RoomServices, RoomServicesAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Review, ReviewAdmin)

