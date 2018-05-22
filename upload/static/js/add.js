var add =(function(){

/*  var array=[
      ["Getting Started"],
      ["Language","html",'javascript','css']
  ];
  var html= ""
  var $list = $("root");
  $list.delegate("#add",'click',Add);

  function render(){
    $list.html()
  }*/


  $('body').on('click', '[data-editable]', function(){

      var $el = $(this);

      var $input = $('<input/>').val( $el.text() );
      $el.replaceWith( $input );

      var save = function(){
        var $p = $('<a data-editable />').text( $input.val() );
        $input.replaceWith( $p );
      };
      $input.one('blur', save).focus();
  });

})();
