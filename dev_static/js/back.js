$(document).ready(function(){
    $('#CallBackModal form button').click(function(e) {  // Обратный звонок
        e.preventDefault();

        csrf_token = $('#CallBackModal form [name="csrfmiddlewaretoken"]').val();
        phone = $('#CallBackModalPhone').val();
        
		data = {
            "csrfmiddlewaretoken": csrf_token,
            phone: phone,
        }

		$.ajax({
			type: "POST",
			url: $('#CallBackModal form').attr('action'),
			data: data,
			success: function(data) {
                $('#CallBackModal form').removeClass('needs-validation');
                $('#CallBackModal form').addClass('was-validated');
                if(data.sended==1) {
                    $('#CallBackModal .modal-form-success').addClass('successed');
                } else if(data.sended==0) {
                    $('#CallBackModal .alert-danger').removeClass('d-none');
                    $('#CallBackModal form button').removeClass('d-block');
                    $('#CallBackModal form button').addClass('d-none');
                }
            }
		});
    });

    $('#SendMessageModal form button').click(function(e) {  // Обратная связь
        e.preventDefault();

        csrf_token = $('#SendMessageModal form [name="csrfmiddlewaretoken"]').val();
        recaptcha = $('#SendMessageModal form [name="g-recaptcha-response"]').val();
        email = $('#id_email').val();
        name = $('#id_name').val();
        message = $('#id_message').val();
        
		data = {
            "csrfmiddlewaretoken": csrf_token,
            'g-recaptcha-response': recaptcha,
            email: email,
            name: name,
            message: message,
        }

		$.ajax({
			type: "POST",
			url: $('#SendMessageModal form').attr('action'),
			data: data,
			success: function(data) {
                $('#SendMessageModal form').removeClass('needs-validation');
                $('#SendMessageModal form').addClass('was-validated');
                if(data.sended==1) {
                    $('#SendMessageModal .modal-form-success').addClass('successed');
                } else if(data.sended==0) {
                    $('#SendMessageModal .alert-danger').removeClass('d-none');
                    $('#SendMessageModal form button').removeClass('d-block');
                    $('#SendMessageModal form button').addClass('d-none');
                } else if(data.sended==3) {
                    $('#SendMessageModal form .alert-danger').removeClass('d-none');
                }
            }
		});
    });

    
});
