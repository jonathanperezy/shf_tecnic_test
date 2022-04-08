odoo.define('shf_tecnic_test.service_guide', function(require){
    "strict";

    const sAnimation = require('website.content.snippets.animation')
    sAnimation.registry.service_guide_list = sAnimation.Class.extend({
        selector: '#service_guide_container',
        start: function(){
            // $('#table_service_guides').DataTable()
        }
    })
})