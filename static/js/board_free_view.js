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
    if(enableCommentWrite) {
        CKEDITOR.replace('editor-comment', {
            resize_enabled: false,
            enterMode: '2',
            shiftEnterMode: '3',
            mathJaxLib: 'http://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_HTML',
            extraPlugins: 'mathjax',
            toolbar: [
                ['Cut','Copy','Paste'],
                ['Undo','Redo','Find','Replace'],
                ['Image','Table','Smiley','SpecialChar','Mathjax'],
                ['Styles','Format','Font','FontSize','TextColor']
            ]
        });
    }
});
function deleteComment(pk) {
    var newForm = $('<form>', {}).append($('<input>', {
        'id': 'id',
        'name' : 'id',
        'value': pk,
        'type' : 'hidden'
    }));
    $.ajax({
        url: '/board/free/comment/delete/',
        type: 'POST',
        data: $(newForm).serialize()
    }).done(function(data) {
        location.reload();
    }).fail(function(data) {
        alert(JSON.stringify(data));
    })
}
function deletePost(pk) {
    var newForm = $('<form>', {}).append($('<input>', {
        'id': 'id',
        'name' : 'id',
        'value': pk,
        'type' : 'hidden'
    }));
    $.ajax({
        url: '/board/free/post/delete/',
        type: 'POST',
        data: $(newForm).serialize()
    }).done(function(data) {
        window.location.href = "/board/free/list";
    }).fail(function(data) {
        alert(JSON.stringify(data));
    })
}