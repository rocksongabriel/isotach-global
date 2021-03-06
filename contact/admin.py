from django.contrib import admin

from .models import Contact, Inquiry, Newsletter, ScheduleMeeting, SiteAdministrator


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["full_name", "city", "phone_number", "email", "date_and_time"]
    search_fields = ["full_name", "city", "email"]
    ordering = ("-date_and_time",)
    readonly_fields = [
        "full_name",
        "city",
        "phone_number",
        "email",
        "date_and_time",
        "message",
    ]


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "signup_date"]
    search_fields = ["full_name", "email"]
    ordering = ("-signup_date",)
    readonly_fields = ["full_name", "email", "signup_date", "phone_number"]


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ["full_name", "phone_number", "email", "submitted",]
    search_fields = ["full_name", "email"]
    readonly_fields = [
        "submitted",
        "full_name",
        "phone_number",
        "email",
        "question",
        "apartment_link",
        "apartment_title",
        "agent_name",
    ]


@admin.register(ScheduleMeeting)
class ScheduleMeetingAdmin(admin.ModelAdmin):
    list_display = ["full_name", "phone_number", "email", "meeting_date_and_time"]
    readonly_fields = [
        "submitted",
        "full_name",
        "phone_number",
        "email",
        "meeting_date_and_time",
        "apartment_link",
        "apartment_title",
        "agent_name"
    ]
    

@admin.register(SiteAdministrator)
class SiteAdministratorAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email"]
