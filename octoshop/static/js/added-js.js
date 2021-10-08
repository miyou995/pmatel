
jQuery(document).ready(function($)
{
	"use strict";

	initThumbnail();
    initQuantity();

	function initThumbnail()
	{
        console.log('loooooded');
		if($('.single_product_thumbnails ul li').length)
		{
			var thumbs = $('.single_product_thumbnails ul li');
			var singleImage = $('.single_product_image_background');

			thumbs.each(function()
			{
				var item = $(this);
				item.on('click', function()
				{
					thumbs.removeClass('active');
					item.addClass('active');
					var img = item.find('img').data('image');
					singleImage.css('background-image', 'url(' + img + ')');
				});
			});
		}	
	}

	function initQuantity()
	{
		if($('.plus').length && $('.minus').length)
		{
			var plus = $('.plus');
			var minus = $('.minus');
			var value = $('#quantity_value');
			var hiddenQte = $('#quantity_hidden');
			plus.on('click', function()
			{
				var x = parseInt(value.text());
				value.text(x + 1);
				hiddenQte.val(value.text()) 
                
			});
			minus.on('click', function()
			{
				var x = parseInt(value.text());
				if(x > 1){
					value.text(x - 1);
                    hiddenQte.val(value.text()) 
				}
			});
            console.log('hiddenQte', hiddenQte);
		}
	}


});