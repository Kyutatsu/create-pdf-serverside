jQuery(function ($) {
    $('#table_id').DataTable({
        "processing": true,
        "serverSide": true,
        "ajax": {
            'url': '/datatable-view/',
            'type': 'GET'
        }
    });

    $('#pdf_button').on('click', function () {
        const table = $('#table_id').DataTable();
        const query_params = table.ajax.params();
        // 1ページあたりのデータ取得件数: -1は全件。
        query_params.length = -1;

        query_string = $.param(query_params);
        const url = '/datatable-view/' + '?' + query_string + '&' + 'output=pdf';
        window.open(url, '_blank');

    });
});
