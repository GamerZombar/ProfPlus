/* global bootstrap: true */
(function () {
  'use strict'
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  tooltipTriggerList.forEach(function (tooltipTriggerEl) {
    new bootstrap.Tooltip(tooltipTriggerEl)
  })
})()


// $( document ).ready( function () {
//     var url = window.location.href.substr( window.location.href.lastIndexOf( '/' ) + 1 );
//     $( '.navbar-nav a' ).each( function () {
//         if( $( this ).attr( 'href' ) === url || $( this ).attr( 'href' ) === '' ) {
//             $( this ).parent( 'li' ).addClass( 'active' );
//         }
//     });
// });