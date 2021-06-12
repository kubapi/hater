$(document).ready(function() {
    $('#ranking_table').DataTable({
        "paging":   false,
        "info":     false,
        "ordering": false,
        language: { 
            "search": "Znajdź swój wynik:",
            "zeroRecords": "Niestety... pusto!",
        },

        //add these config to remove empty header
        "bJQueryUI": true,
        "sDom": 'lfrtip'
    });
} );

