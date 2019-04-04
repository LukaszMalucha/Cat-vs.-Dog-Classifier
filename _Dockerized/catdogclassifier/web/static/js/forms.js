$(function() {
    $('#upload-file-btn').click(function() {
        var form_data = new FormData($('#upload-file')[0]);
        $('.loader').show();
        $('#cat').hide();
        $('#dog').hide();
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                $('.loader').hide();
                if (data.guess === 'Cat') {

                        $('#cat').show();

                }

                else if (data.guess === 'Dog') {
                        $('#dog').show();

                }

                else {
                    $('#error').text(data.error).show();

                }

                $(".card-prediction").delay(3000).fadeOut(1000, function() {
                            $(this).alert('close');
                        });

                $("#error").delay(3000).fadeOut(1000, function() {
                            $(this).alert('close');
                        });


            },
        });
    });
});
