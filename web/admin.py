from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class provinceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nama', 'province_id')
    search_fields = ['nama', 'province_id']
    readonly_fields = ('date_created', 'date_modified')
admin.site.register(province, provinceAdmin)

class districtAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nama','Province', 'city_id')
    search_fields = ['nama', 'city_id']
    readonly_fields = ('date_created', 'date_modified')
    autocomplete_fields = ['Province']
admin.site.register(distrcit_city, districtAdmin)

class subdistrictAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nama','subdistrict_id','district', 'get_Province', )
    search_fields = ['nama', 'subdistrict_id']
    readonly_fields = ('date_created', 'date_modified')
    autocomplete_fields = ['district']

    def get_Province(self, obj):
        return obj.district.Province.nama
    get_Province.admin_order_field  = 'province'  #Allows column order sorting
    get_Province.short_description = 'Province Name' 
admin.site.register(sub_district, subdistrictAdmin)

class villageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nama','village_id','sub_district','get_district', 'get_Province', )
    search_fields = ['nama', 'village_id']
    readonly_fields = ('date_created', 'date_modified')
    autocomplete_fields = ['sub_district']

    def get_district(self, obj):
        return obj.sub_district.district.nama
    get_district.admin_order_field  = 'district'  #Allows column order sorting
    get_district.short_description = 'district Name' 

    def get_Province(self, obj):
        return obj.sub_district.district.Province.nama
    get_Province.admin_order_field  = 'province'  #Allows column order sorting
    get_Province.short_description = 'Province Name' 
    
admin.site.register(village, villageAdmin)

class actoradmin( admin.TabularInline):
    model = incident_actor

class violenceadmin( admin.TabularInline):
    model = violence_form
    autocomplete_fields = ['category', 'event']

class weaponadmin( admin.TabularInline):
    model = Weapon_form
    autocomplete_fields = ['category', 'event']

class issueadmin( admin.TabularInline):
    model = Issue_Type
    autocomplete_fields = ['category', 'event']

class interveneadmin( admin.TabularInline):
    model = Intervene_actions
    autocomplete_fields = ['incident_event']

class IncidentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = [
        actoradmin, violenceadmin, weaponadmin, issueadmin, interveneadmin
    ]
    list_display = ('incident_id', 'related', 'area_subdistrict', 'area_village','covid_rel', 'num_death', 'num_injured', 'death_injured','fem_death', 'fem_injured', 'child_death', 'child_injured', 'Infra_damage', 'Infra_destroyed', 'intervene')
    search_fields = ['incident_id']
    autocomplete_fields = ['related', 'area_village', 'area_subdistrict', 'area_district']
 #   readonly_fields = ('date_created', 'date_modified')
    
admin.site.register(incident, IncidentAdmin)

class actorcategoryadmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields= ['nama']
admin.site.register(actor_category, actorcategoryadmin)

class incidentactorAdmin_1(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('incident_events','actor', 'actor_category', 'actor_vm', 'actor_Total', )
    search_fields = ['nama', 'city_id']
    readonly_fields = ('date_created', 'date_modified')
    autocomplete_fields = ['incident_events']
admin.site.register(incident_actor, incidentactorAdmin_1)

class violencecategoryadmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields= ['nama']
admin.site.register(violence_category, violencecategoryadmin )

class violenceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('category','event' )
    search_fields = ['category', 'event']
    readonly_fields = ('date_created', 'date_modified')
    autocomplete_fields = ['category', 'event']
admin.site.register(violence_form, violenceAdmin)

class weaponcategoryadmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields= ['nama']
admin.site.register(Weapon_category, weaponcategoryadmin)

class WeaponFormAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('category','event' )
    search_fields = ['category', 'event']
    autocomplete_fields = ['category', 'event']
    readonly_fields = ('date_created', 'date_modified')
admin.site.register(Weapon_form, WeaponFormAdmin)

class issuecategoryadmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields= ['nama']
admin.site.register(Issue_category, issuecategoryadmin)

class IssueAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('category','event' )
    search_fields = ['category', 'event']
    autocomplete_fields = ['category', 'event']
    readonly_fields = ('date_created', 'date_modified')
admin.site.register(Issue_Type, IssueAdmin)

class InterveneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('actor_category','actor', 'incident_event' )
    search_fields = ['actor_category', 'actor', 'incident_event']
    autocomplete_fields = ['incident_event']
    readonly_fields = ('date_created', 'date_modified')
admin.site.register(Intervene_actions, InterveneAdmin)


'''class projectadmin(admin.ModelAdmin):
    list_display = ('title', 'dept','member', 'periode_start', 'periode_end', 'publish')
    list_filter = ('publish','department')
    search_fields = ['title','department','project_member' ]
    date_hierarchy = 'date_created'
    readonly_fields = ('date_created', 'date_modified')
    autocomplete_fields = ['department', 'project_member']
    def member(self, obj):
        return "\n, ".join([p.name for p in obj.project_member.all()])
        
    def dept(self, obj):
        return "\n, ".join([p.name for p in obj.department.all()])
      
    
admin.site.register(Project, projectadmin)'''