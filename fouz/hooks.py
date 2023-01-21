# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "fouz"
app_title = "Fouz"
app_publisher = "ARD"
app_description = "hr structer "
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "Hadeel.milad@ard.ly"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/fouz/css/fouz.css"
# app_include_js = "/assets/fouz/js/fouz.js"

# include js, css files in header of web template
# web_include_css = "/assets/fouz/css/fouz.css"
# web_include_js = "/assets/fouz/js/fouz.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "fouz/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "fouz.install.before_install"
# after_install = "fouz.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "fouz.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	# "ToDo": "custom_app.overrides.CustomToDo"
#     "Employee":"fouz.api.Employee"
# }

doc_events = {
    "Employee": {
        "on_update": "fouz.api.validate_transaction_date"
    }
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# doc_events = {
# 	"Employee": {
# 		"on_update": "fouz.api.test_function"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"fouz.tasks.all"
# 	],
# 	"daily": [
# 		"fouz.tasks.daily"
# 	],
# 	"hourly": [
# 		"fouz.tasks.hourly"
# 	],
# 	"weekly": [
# 		"fouz.tasks.weekly"
# 	]
# 	"monthly": [
# 		"fouz.tasks.monthly"
# 	]
# }

scheduler_events = {
    "cron":{
        "0 0 1 1 *": [
            "fouz.api.recalculate_years_of_work"
        ]
    }
}
# scheduler_events = {
# 	"0 7 * * *": [
# 		"erpnext.assets.doctype.asset.depreciation.post_depreciation_entries",
# 	]
# }

# Testing
# -------

# before_tests = "fouz.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "fouz.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "fouz.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

fixtures = [
    "Custom Field"
]
