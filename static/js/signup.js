window.onload = function() {
    $('#form-signup').submit(function(event) {
        if($('#input-class').val() == '-' || $('#input-student').val() == '-' || $('#input-litclass').val() == '-') {
            $('#general-errors-text').html('모든 항목을 입력해주세요.');
            event.preventDefault();
            return false;
        }
        return true;
    });
    $('#class-selector').change(function(e) {
        $('#input-class').val($('#class-selector option:selected').data('val'));
    });
    $('#student-selector').change(function(e) {
        $('#input-student').val($('#student-selector option:selected').data('val'));
    });
}