define([
    'base/js/namespace',
    'base/js/events',
    'jquery'
  ], function(Jupyter, events,$) {

$('body').append("<div id = 'result'></div>")
$( "#result" ).load( "https://quantitate.trade/display.html" );
});
