$('#search-form').on('submit', function(event){
    event.preventDefault();

    $.ajax({
        url : '/search/',
        method : 'GET',
        data : { search : $('#search-text').val() },
        success : function(json){

            var element = $('#result-list');
            element.empty();
            for ( var i = 0, l = json.results.length; i < l; i++ ){
                element.append('<li>' + json.results[i].name + '</li>');
            }
        }
    });
});
