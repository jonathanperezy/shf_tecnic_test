odoo.define('shf_tecnic_test.service_guide', function(require){
    "strict";

    const sAnimation = require('website.content.snippets.animation'),
          rpc = require('web.rpc');

    sAnimation.registry.service_guide_list = sAnimation.Class.extend({
        selector: '#service_guide_container',
        read_events:{
            'click button.grouper': 'group_by'
        },
        start: function(){
            this.tab_selector = '#table_service_guides'
            this.$table = $(this.tab_selector).DataTable({
                columnDefs: [{visible: true, targets: [2, 3, 4]}],
            })
        },

        group_by: function(e){
            let attrow = parseInt( this.$(e.currentTarget).attr('row') ),
                api = $.fn.dataTable.Api(this.tab_selector),
                rows = api.rows({page:'current'}).nodes(),
                last = null;

            $('tbody tr.group').each((i, tr) => $(tr).remove())
            let totals = {}
            let data = api.column(attrow, {page: 'current'} ).data()
            for(const key in data){
                if(!isNaN(key)){
                    let group = data[key]
                    if ( typeof totals[group] == 'undefined'){
                        totals[group] = 0
                    }
                    totals[group] += parseFloat( $(rows[key].children[5]).text().trim() )
                    if ( last !== group ) {
                        let tr = '<tr class="group bg-dark-light"><td colspan="5"><strong>' + group + '</strong></td><td class="groupable" for="'+ group +'"></td></tr>'
                        $(rows).eq(key).before( tr ); 
                        last = group; 
                    }
                }
            }
            $('td.groupable').each((index, td) => {
                $(td).html('<strong>( ' + totals[$(td).attr('for')] + ' )</strong>' )
            })
        },
    })

    sAnimation.registry.service_guide_form = sAnimation.Class.extend({
        selector: '#service_guide_form',
        read_events:{
            // 'click button#edit': 'click_make_editable',
        },
        start: function(){
            this.$save_btn = this.$('button#save')
            this.$edit_btn = this.$('button#edit')
            this.$cancel_btn = this.$('button#cancel')
            this.$observ_p = this.$('p#observations')
            
            this.on_click_make_editable()
        },

        on_click_make_editable: function(){
            let self = this;
            this.$edit_btn.unbind('click').on('click', function(){
                $(this).attr('disabled', true).hide()
                self.make_invisible($(this))
                self.make_visible(self.$save_btn)
                self.make_visible(self.$cancel_btn)
                self.$observ_p.attr('contenteditable', true)
                self.$observ_p.focus()
                self.$observ_p.addClass('editable')
                self.on_click_save_description()
                self.on_click_cancel()
            })
        },

        on_click_save_description: function(){
            let self = this
            this.$save_btn.unbind('click').on('click', function(){
                let id = parseInt(self.$(this).data('record_id'))
                rpc.query({
                    model: 'shf.service.guide',
                    method: 'write',
                    args: [[id], {'observations': self.$observ_p.text().trim() }]
                }).then( res => self.backward_elements() )
            })
        },

        on_click_cancel: function(){
            let self = this
            this.$cancel_btn.unbind('click').on('click', () => self.backward_elements() );
        },

        backward_elements: function(){
            this.make_invisible(this.$save_btn)
            this.make_invisible(this.$cancel_btn)
            this.make_visible(this.$edit_btn)
            this.$observ_p.attr('contenteditable', false)
            this.$observ_p.removeClass('editable')
            this.on_click_make_editable()
        },

        make_visible: function(button){
            button.attr('disabled', false).show()
        },

        make_invisible: function(button){
            button.attr('disabled', true).hide()
            button.unbind('click')
        }
    })
})