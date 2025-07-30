from odoo import http
from odoo.http import request
import datetime
import json


class AttendanceAPIController(http.Controller):

    def _is_valid_api_key(self, api_key):
        system_key = request.env["ir.config_parameter"].sudo().get_param("attendance_api_key")
        return api_key == system_key

    @http.route("/api/today_attendance", type="json", auth="none", csrf=False)
    def today_attendance_json(self, **kwargs):
        api_key = kwargs.get("api_key")
        if not self._is_valid_api_key(api_key):
            return {"error": "Unauthorized: Invalid API key"}

        today = datetime.date.today()
        start = datetime.datetime.combine(today, datetime.time.min)
        end = datetime.datetime.combine(today, datetime.time.max)

        attendance_records = request.env["hr.attendance"].sudo().search([
            ("check_in", ">=", start),
            ("check_in", "<=", end),
        ])

        result = {}
        for att in attendance_records:
            emp = att.employee_id.name
            if emp not in result:
                result[emp] = {"check_in": att.check_in, "check_out": att.check_out}
            else:
                # Choose the earliest check-in and latest check-out
                if att.check_in and att.check_in < result[emp]["check_in"]:
                    result[emp]["check_in"] = att.check_in
                if att.check_out and (not result[emp]["check_out"] or att.check_out > result[emp]["check_out"]):
                    result[emp]["check_out"] = att.check_out

        return {"status": "success", "data": result}

    @http.route("/today-attendance", type="http", auth="public", website=True)
    def website_today_attendance(self, **kwargs):
        today = datetime.date.today()
        start = datetime.datetime.combine(today, datetime.time.min)
        end = datetime.datetime.combine(today, datetime.time.max)

        attendance_records = request.env["hr.attendance"].sudo().search([
            ("check_in", ">=", start),
            ("check_in", "<=", end),
        ])

        data = {}
        for att in attendance_records:
            emp = att.employee_id.name
            if emp not in data:
                data[emp] = {"check_in": att.check_in, "check_out": att.check_out}
            else:
                if att.check_in and att.check_in < data[emp]["check_in"]:
                    data[emp]["check_in"] = att.check_in
                if att.check_out and (not data[emp]["check_out"] or att.check_out > data[emp]["check_out"]):
                    data[emp]["check_out"] = att.check_out

        return request.render("attendance_api_rpc.today_attendance_template", {"attendance_data": data})
