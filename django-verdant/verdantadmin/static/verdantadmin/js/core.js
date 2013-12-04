$(function(){
    // Enable toggle to open/close nav
    $('#nav-toggle').click(function(){ 
        $('body').toggleClass('nav-open');
    });

    // Enable swishy section navigation menu
    $('.explorer').addClass('dl-menuwrapper').dlmenu({
        animationClasses : {
            classin : 'dl-animate-in-2', 
            classout : 'dl-animate-out-2'
        } 
    });

    // Resize nav to fit height of window. This is an unimportant bell/whistle to make it look nice
    var fitNav = function(){
        $('.nav-wrapper').css('min-height',$(window).height())
    }
    fitNav();
    $(window).resize(function(){
        fitNav();
    })

    // Apply auto-height sizing to text areas
    // NB .richtext (hallo.js-enabled) divs do not need this as they expand to fit their content by default
    // $('.page-editor textarea').autosize();

    // Enable nice focus effects on all fields. This enables help text on hover.
    $(document).on('focus mouseover', 'input,textarea,select', function(){
    	$(this).closest('.field').addClass('focused')
    	$(this).closest('fieldset').addClass('focused')
        $(this).closest('li').addClass('focused')
    })
    $(document).on('blur mouseout', 'input,textarea,select', function(){
    	$(this).closest('.field').removeClass('focused')
    	$(this).closest('fieldset').removeClass('focused')
        $(this).closest('li').removeClass('focused')
    });

    /* tabs */
    $(document).on('click', '.tab-nav a', function (e) {
        e.preventDefault()
        $(this).tab('show');
    });   
    $(document).on('click', '.tab-toggle', function(e){
        e.preventDefault()
        $('.tab-nav a[href="'+ $(this).attr('href') +'"]').click();
    })

    // Add class to the body from which transitions may be hung so they don't appear to transition as the page loads
    $('body').addClass('ready'); 

    $('.dropdown-toggle').bind('click', function(){
        $(this).closest('.dropdown').toggleClass('open');

        // Stop event propagating so the "close all dropdowns on body clicks" code (below) doesn't immediately close the dropdown
        return false;
    });

    /* close all dropdowns on body clicks */
    $(document).on('click', function(e){
        var relTarg = e.relatedTarget || e.toElement;
        if(!$(relTarg).hasClass('dropdown-toggle')){
            $('.dropdown').removeClass('open');
        }
    })

    /* Bulk-selection */
    $(document).on('click', 'thead .bulk', function(){
        $(this).closest('table').find('tbody .bulk input').each(function(){
            $(this).prop('checked', !$(this).prop('checked'));            
        })
    });

    $('.listing tbody td').click(function(){
        document.location.href = $(this).parent().find('.title a').attr("href")
    })
})