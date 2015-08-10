/* -----------------------------------------------------------------------------
 * /daily-tasks/
 * ---------------------------------------------------------------------------*/
function init_datepicker() {
    var date = new Date();
    var today = date.getFullYear() + '-' +  (date.getMonth() + 1) + '-' + date.getDate();
    var previous_date = today;
    get_daily_stats(today);
    
    $('#datepicker').datepicker({
        format: 'yyyy-mm-dd',
        startDate: "2014-10-13",
        endDate: '0d'
    }).on('changeDate', function(){
        var new_date = $('#datepicker').datepicker('getDate');
        if ( isNaN( new_date.getTime() ) ) {
            $('#datepicker').datepicker('setDate', previous_date);
        } else {
            new_date = new_date.getFullYear() + '-' +  (new_date.getMonth() + 1) + '-' + new_date.getDate();
            previous_date = new_date;
            get_daily_stats(new_date);
        }
    });
    $('#datepicker').datepicker('setDate', today);

}
function init_stats_form() {
    var frm = $('#save-daily-task');
    frm.submit(function () {
        $.ajax({
            type: 'POST',
            url: '/daily-tasks/',
            data: frm.serialize()+"&steps="+$('#id_steps').val(),
            success: function (data) {
                get_daily_stats($('#id_date').val());
                console.log(data);
            },
            error: function(data) {
                console.log(data);
            }
        });
        return false;
    });
    
    var step_btn = $('#update_steps');
    step_btn.click(function() {
        var date = $('#id_date').val();
        $.ajax({
            type: 'POST',
            url: '/ajax/update-steps/',
            data: "date="+date,
            success: function (data) {
                get_daily_stats(date);
                console.log(data);
            },
            error: function(data) {
                console.log(data);
            }
        });
        return false;
    });
}
function get_daily_stats(date) {
    $.ajax({ 
        type: 'POST',
        url: '/ajax/get-daily-stats/', 
        data: {'date':date},
        dataType: "json",
        success: function(data) { 
            console.log(data);
            var json = $.parseJSON(data);
            var field = json[0].fields;
            $('#id_pushups').val(field.pushups);
            $('#id_pushups-icon').html(get_icon('pushups', field.pushups));
            $('#id_situps').val(field.situps);
            $('#id_situps-icon').html(get_icon('situps', field.situps));
            $('#id_squats').val(field.squats);
            $('#id_squats-icon').html(get_icon('squats', field.squats));
            $('#id_date').val(date);
            
            $('#id_steps').val(field.steps);
            $('#id_steps-icon').html(get_icon('steps', field.steps));
        },
        error: function(error){
            if (error != 'DoesNotExist') {
                console.log("Error:");
                console.log(error);
            }
        }
    });
}
function get_icon(field, val) {
    var status = false;
    
    switch (field) {
        case 'pushups':
            status = (val >= 50);
            break;
        case 'situps':
            status = (val >= 50);
            break;
        case 'squats':
            status = (val >= 50);
            break;
        case 'steps':
            status = (val >= 10000);
            break;
    }

    if (status) {
        return '<i class="icon-lifefull"></i>'
    } else {
        return '<i class="icon-lifeempty"></i>'
    }
}