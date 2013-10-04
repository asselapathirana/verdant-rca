(function() {
    var panel = InlinePanel({
        formsetPrefix: fixPrefix("id_{{ self.formset.prefix }}"),
        emptyChildFormPrefix: fixPrefix("{{ self.empty_child.form.prefix }}"),
        canOrder: {% if self.can_order %}true{% else %}false{% endif %},

        onAdd: function(fixPrefix) {
            {{ self.empty_child.render_js }}
        }
    });

    {% for child in self.children %}
        {{ child.render_js }}
        panel.initInlineChildDeleteButton(fixPrefix("{{ child.form.prefix }}"));
    {% endfor %}
})();
