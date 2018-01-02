function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
var csrftoken = 123123
$(document).ready(function() {
    csrftoken = $("[name=csrfmiddlewaretoken]").val();
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});
function deletePost(pk) {
    var newForm = $('<form>', {}).append($('<input>', {
        'id': 'id',
        'name' : 'id',
        'value': pk,
        'type' : 'hidden'
    }));
    $.ajax({
        url: '/homework/delete/',
        type: 'POST',
        data: $(newForm).serialize()
    }).done(function(data) {
        window.location.href = "/homework/list/"+class_no.toString();
    }).fail(function(data) {
        alert(JSON.stringify(data));
    })
}