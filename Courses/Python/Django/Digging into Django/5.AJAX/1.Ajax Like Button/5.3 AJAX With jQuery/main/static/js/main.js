$('#search-form').on('submit', function(event){
    event.preventDefault();

    $.ajax({
        url : '/search/',
        method : 'GET',
        data : { search : $('#search-text').val() },

        success : function(json){
            alert(JSON.stringify(json));
        }
    });
});
