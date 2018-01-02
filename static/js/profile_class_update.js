function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        csrftoken = $("[name=csrfmiddlewaretoken]").val();
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function showToast(text) {
    $('#ok-toast').text(text);
}

function changeClassValue(pk, value) {
    var newForm = $('<form>', {}).append($('<input>', {
        'id': 'change_class',
        'name' : 'change_class',
        'value': pk,
        'type' : 'hidden'
    })).append($('<input>', {
        'id': 'class_value',
        'name' : 'class_value',
        'value': value,
        'type' : 'hidden'
    }));
    $.ajax({
        url: '/profile/update/class/',
        type: 'POST',
        data: $(newForm).serialize()
    }).done(function(data) {
        // TODO: fading OK sign
        showToast("수업이 변경되었습니다.");
    }).fail(function(data) {
        alert(JSON.stringify(data));
    })
}
$(".cledit-checkbox").change(function(e) {
    classID = parseInt($(e.currentTarget).data("pk"));
    if($(e.currentTarget).is(":checked")) {
        changeClassValue(classID, 1);
    } else {
        changeClassValue(classID, 0);
    }
});