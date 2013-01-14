$(function () {
    $(window).scroll(function(){
        // add navbar opacity on scroll
        if ($(this).scrollTop() > 100) {
            $(".navbar.navbar-fixed-top").addClass("scroll");
        } else {
            $(".navbar.navbar-fixed-top").removeClass("scroll");
        }

        // global scroll to top button
        if ($(this).scrollTop() > 300) {
            $('.scrolltop').fadeIn();
        } else {
            $('.scrolltop').fadeOut();
        }
    });

    // scroll back to top btn
    $('.scrolltop').click(function() {
        $("html, body").animate({ scrollTop: 0 }, 700);
        return false;
    });

    // scroll navigation functionality
    $('.scroller').click(function() {
        var hash = this.hash.substring(1),
            elementOnPage = $('[name="' + hash + '"]');

        // Just follow the regular link if the section is not on the current page.
        if (elementOnPage.length) {
            var top = elementOnPage.offset().top;
            $("html, body").animate({ scrollTop: top }, 700, function () { window.location.hash = hash; });
            return false;
        }
    });

    // FAQs
    var $faqs = $("#faq .faq");
    $faqs.click(function () {
        var $answer = $(this).find(".answer");
        $answer.slideToggle('fast');
    });

    if (!$.support.leadingWhitespace) {
        //IE7 and 8 stuff
        $("body").addClass("old-ie");
    }

    $('.blog_post .post_content p img, .container .markdown p img').each(function() {
        $(this).wrap('<figure class="image"></figure>');
        if ($(this).attr("alt"))
            $(this).after('<figcaption>'+$(this).attr("alt")+'</figcaption>');
    });
});