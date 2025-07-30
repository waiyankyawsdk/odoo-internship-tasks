/** @odoo-module **/

import { rpc } from "@web/core/network/rpc";

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.vip-button').forEach(button => {
        button.addEventListener('click', async () => {
            const partnerId = button.getAttribute('data-partner-id');
            if (!partnerId || isNaN(partnerId)) {
                alert(' Invalid Partner ID!');
                return;
            }

            try {
                await rpc.query({
                    model: 'res.partner',
                    method: 'mark_as_vip',
                    args: [[parseInt(partnerId)]],
                });
                alert(" Marked as VIP!");
                window.location.reload();
            } catch (error) {
                alert(" Failed to mark as VIP.");
                console.error(error);
            }
        });
    });
});
