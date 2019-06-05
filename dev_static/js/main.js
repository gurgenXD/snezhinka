(function($) {
    function FooterBottom() { 
        $('body').css('margin-bottom', $('.footer').outerHeight())
    };

    FooterBottom();
    window.addEventListener('resize', FooterBottom, false);  
})(jQuery);

$(function () {
    $(".zoom-image").SmartPhoto();
});

$(document).ready(function(){
    $(".dropdown").hover(            
        function() {
            $('.dropdown-menu', this).not('.in .dropdown-menu').stop( true, true ).delay(50).slideDown("fast");
            $(this).toggleClass('open');
        },
        function() {
            $('.dropdown-menu', this).not('.in .dropdown-menu').stop( true, true ).delay(50).slideUp("fast");
            $(this).toggleClass('open');
        }
    );
});

$(function () {
    'use strict'
    $('[data-toggle="offcanvas"]').on('click', function () {
        $('.offcanvas-collapse').toggleClass('open')
    })
});

$(function() {
    Stickyfill.add($('.sticky'));
});

$(document).ready(function(){
    $(window).scroll(function(){
        if ($(this).scrollTop() > 400) {
            $('.scroll-to-top').fadeIn(200);
        } 
        else {
            $('.scroll-to-top').fadeOut(200);
        }
    });
    $('.scroll-to-top').click(function(){
        $('html, body').animate({scrollTop : 0},300);
        return false;
    });
});

(function() {
    'use strict';
    window.addEventListener('load', function() {
        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.getElementsByClassName('needs-validation');
        // Loop over them and prevent submission
        var validation = Array.prototype.filter.call(forms, function(form) {
            form.addEventListener('submit', function(event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();

jQuery(function($){
    $("#CallBackModalPhone").mask("+7 999 999 99 99",{placeholder:"*"});
    $("#ConsumerStockPhone").mask("+7 999 999 99 99",{placeholder:"*"});
});

$(document).ready(function(){
    $('.close-all').on('click',function() {
        $('.modal').modal('hide');
    })
});

$(document).ready(function(){
    $('.navbar-toggler').on('click',function() {
        $(this).toggleClass('active');
    })
});

(function($) {
    function mediaSize() { 
        if (window.matchMedia('(max-width: 991.98px)').matches) {
            $('.navbar-expand-lg').addClass('sticky shadow-sm');

        } else {
            $('.navbar-expand-lg').removeClass('sticky shadow-sm');
        }
    };

    mediaSize();
    window.addEventListener('resize', mediaSize, false);  
})(jQuery);

$(function() {
    $('.eq-h').matchHeight({
        byRow:true
    });
});

$(function() {
    $('.newsfeed-item').matchHeight({
        byRow:true
    });
});

$(document).ready(function(){
    $('.sp-wrap').smoothproducts();
});

$(document).ready(function(){
    $("input[type='number']").inputSpinner();
});