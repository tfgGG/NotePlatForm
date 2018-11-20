$( document ).ready(function(){

    $( ".sortable" ).sortable({
        connectWith: ".sortlist",
    });
    $( ".sortable" ).disableSelection();
    $('.ui.dropdown').dropdown();

   
})

