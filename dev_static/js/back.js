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

    $('.size_button').click(function() {  // Изменение размера
        product_id = $('#product-prop-form').data('product-id');
        size_value = $(this).children('input').val();
        material_value = $('.material_button.active input').val();
        csrf_token = $('#product-prop-form [name="csrfmiddlewaretoken"]').val();

		data = {
            "csrfmiddlewaretoken": csrf_token,
            product_id: product_id,
            size_value: size_value,
            material_value: material_value,
        }

        $.ajax({
        	type: "POST",
        	url: $('#product-prop-form').attr('action'),
        	data: data,
            success: function(data) {
                if (data.offer_price_without_sale == data.offer_price) {
                    $('.product-price-div').html('<span class="product-price h3 font-2 text-dark">' + data.offer_price + '<i class="fas fa-ruble-sign fa-xs ml-1"></i></span>')
                } else {
                    $('.product-price-div').html('<span class="product-price h4 font-2 font-weight-normal text-muted mr-2"><del>' + data.offer_price_without_sale +
                                                 '</del></span><span class="product-price h3 font-2 text-danger">' + data.offer_price +
                                                 '<i class="fas fa-ruble-sign fa-xs ml-1"></i></span>')
                }
        	}
        });
    });

    $('.material_button').click(function() { // Изменение материала
        product_id = $('#product-prop-form').data('product-id');
        material_value = $(this).children('input').val();
        size_value = $('.size_button.active input').val();
        csrf_token = $('#product-prop-form [name="csrfmiddlewaretoken"]').val();

		data = {
            "csrfmiddlewaretoken": csrf_token,
            product_id: product_id,
            size_value: size_value,
            material_value: material_value,
        }
        
        $.ajax({
        	type: "POST",
        	url: $('#product-prop-form').attr('action'),
        	data: data,
            success: function(data) {
                if (data.offer_price_without_sale == data.offer_price) {
                    $('.product-price-div').html('<span class="product-price h3 font-2 text-dark">' + data.offer_price + '<i class="fas fa-ruble-sign fa-xs ml-1"></i></span>')
                } else {
                    $('.product-price-div').html('<span class="product-price h4 font-2 font-weight-normal text-muted mr-2"><del>' + data.offer_price_without_sale +
                                                 '</del></span><span class="product-price h3 font-2 text-danger">' + data.offer_price +
                                                 '<i class="fas fa-ruble-sign fa-xs ml-1"></i></span>')
                }
        	}
        });
    });

    $('#add-to-cart button').click(function(e) { // Добавить в корзину
        e.preventDefault();

        product_id = $('#add-to-cart button').data('product-id');
        material_value = $('.material_button.active input').val();
        size_value = $('.size_button.active input').val();
        csrf_token = $('#add-to-cart [name="csrfmiddlewaretoken"]').val();

		data = {
            "csrfmiddlewaretoken": csrf_token,
            product_id: product_id,
            material_value: material_value,
            size_value: size_value,
        }

        $.ajax({
        	type: "POST",
        	url: $('#add-to-cart').attr('action'),
        	data: data,
            success: function(data) {
                $('.cart-len').html(data.cart_len);
        	}
        });
    });

    $('.remove-from-cart a').click(function() { // Удалить из корзины
        offer_id = $(this).data('offer-id');

		data = {
            offer_id: offer_id,
        }

        $.ajax({
        	type: "GET",
        	url: $(this).parent('.remove-from-cart').attr('action'),
        	data: data,
            success: function(data) {
                $('.cart-item-' + data.offer_id).addClass('d-none');
                $('.total-price').html(data.total_price + '<i class="fas fa-ruble-sign fa-xs ml-1"></i>');
                $('.cart-len').html(data.cart_len);
        	}
        });
    });

    function change_quantity() { // Изменить количество товара
        offer_id = $(this).parent().siblings().data('offer-id');
        quantity = $(this).parent().siblings().val();
        console.log(offer_id, quantity)

		data = {
            offer_id: offer_id,
            quantity: quantity,
        }

        $.ajax({
        	type: "GET",
        	url: $(this).parent().parent().attr('action'),
        	data: data,
            success: function(data) {
                $('.cart-item-' + offer_id + ' .offer-cost').html(data.offer_cost + '<i class="fas fa-ruble-sign fa-xs ml-1"></i>');
                $('.total-price').html(data.total_price + '<i class="fas fa-ruble-sign fa-xs ml-1"></i>');
                $('.cart-len').html(data.cart_len);
        	}
        });
    }

    $('.change-quantity-from input').on('blur', change_quantity);
    $('.change-quantity-from .input-group-append').on('click', change_quantity);
    $('.change-quantity-from .input-group-prepend').on('click', change_quantity);
});
