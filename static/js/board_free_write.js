window.onload = function() {
    CKEDITOR.replace('editor-post', {
        enterMode: '2',
        shiftEnterMode: '3',
        mathJaxLib: 'http://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_HTML',
        extraPlugins: 'mathjax',
        toolbar: [
            ['Cut','Copy','Paste','Undo','Redo','Find','Replace'],
            ['Link','Unlink'],
            ['Image','Table','Smiley','SpecialChar','Mathjax'],
            ['Bold','Italic','Strike','RemoveFormat'],
            ['Styles','Format','Font','FontSize','TextColor']
        ]
    });
};
function categoryChanged() {
    $('#input-category').val($('#category-selector').attr('data-val'));
}