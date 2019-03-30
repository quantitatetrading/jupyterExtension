define([
    'base/js/namespace',
    'base/js/events',
    'jquery'
  ],
function(Jupyter, events, $) {

  $('body').append("<div id = 'result'></div>")
  $( "#result" ).load( "https://quantitate.trade/display.html" );

  // Adds a cell above current cell (will be top if no cells)
  var add_cell = function() {
    Jupyter.notebook.
    insert_cell_above('code').
  // Define default cell here
    set_text(`
from trader import *
import pandas as pd
import numpy as np
    `);
    Jupyter.notebook.select_prev();
    Jupyter.notebook.execute_cell_and_select_below();
  };

  // Run on start
  function load_ipython_extension() {
  // Add a default cell if there are no cells
    if (Jupyter.notebook.get_cells().length===1){
        add_cell();
      }
  }

  return {
  load_ipython_extension: load_ipython_extension
  };

});
