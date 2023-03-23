from odoo import http
from odoo.http import request


class HotelGuest(http.Controller):

    @http.route('/hotel/guest', auth='public', website=True)
    def hotel_guest(self):
        guests = request.env['hotel.guest'].sudo().search([])
        return request.render("hotel_management.hotel_website_guest", {
            'guests' : guests
        })

    @http.route('/hotel_guest_form', type="http", auth='public', website=True)
    def hotel_guest_form(self, **kwargs):
        return http.request.render('hotel_management.hotel_guest_form_create', {})

    @http.route('/create/webguest', type="http", auth='public', website=True)
    def create_webguest(self, **kwargs):
        request.env['hotel.guest'].sudo().create(kwargs)
        return http.request.render('hotel_management.website_guest_thanks', {})
