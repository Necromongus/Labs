$(function () {
    $('#id_subject').change(function () {
        if ($("option:selected", this).text() === "Не выбрано")
        {
            $('#id_hotel').attr("disabled", true).prop('selectedIndex',0);
        }
        else
        {
            $('#id_hotel').attr("disabled", false);
            var url = "/db/tutors/" + $(this).val() + "/related_json_tutors";
            $.getJSON(url, function(tutors) {
                var options = '<option value="" selected>Не выбрано</option>';
                for (var i = 0; i < tutors.length; i++) {
                    options += '<option value="' + tutors[i].pk + '">' + tutors[i].fields['surname'] + " " +
                        tutors[i].fields['name'] + " " + tutors[i].fields['patronymic'] + '</option>';
                }
                $("#id_hotel").html(options);
            });
        }
    });


    if ((window.location.pathname) === '/main/') {
        $('.navbar').css({"background-color": "rgba(0,0,0,0.6)"})
    }


    var objects_per_page = parseInt($('#per-page').text());
    var count_current_objects = parseInt($('#per-page').text());
    var courses = [];
    $.getJSON("/db/courses/all_json_courses", function (data) {
        $.each(data, function (i, course) {
            courses.push(course);
        })
    });
    $('.pagination').hide();
    $(document).scroll(function () {
        var curScroll = $(this).scrollTop();
        var maxScroll = document.body.scrollHeight - $(window).height();
        if (curScroll === maxScroll)
        {
            if (count_current_objects < courses.length-1)
            {
                for (var i = count_current_objects; i < objects_per_page+count_current_objects; i++)
                {
                    if (courses[i].fields.photo)
                    {
                        $('.course').append("<a href=\"/courses/" + courses[i].pk + "\" class=\"course-element\">" +
                            "<div class=\"course-photo\">" +
                            "<img class=\"img-course\" src=\"/media/" + courses[i].fields.photo +
                            "\" width=\"100%\" height=\"100%\">" +
                            "</div><span class=\"course-hotel_name\">" + courses[i].fields.name_course + "</span>\n" +
                            "                                <span class=\"course-tutor\">" + courses[i].fields.tutor +
                            "</span></a>");
                    }
                    else
                    {
                        $('.course').append("<a href=\"/courses/" + courses[i].pk + "\" class=\"course-element\">" +
                            "<div class=\"course-photo\"></div>" +
                            "<span class=\"course-hotel_name\">" + courses[i].fields.name_course + "</span>\n" +
                            "                                <span class=\"course-tutor\">" + courses[i].fields.tutor +
                            "</span></a>");
                    }
                    if (i === courses.length-1)
                    {
                        break;
                    }
                }
                $(this).scrollTop(document.body.scrollHeight - $(window).height() - 900);
                count_current_objects = i;
            }
        }
    });


    $('#id_name_course, #id_subject, #id_hotel').on("invalid", function (e) {
        e.preventDefault();
    });
    $('#id_name_course').click(function () {
        $('#error_name_course').fadeOut(2000);
    });
    $('#id_subject').click(function () {
        $('#error_subject_course').fadeOut(2000);
    });
    $('#id_hotel').click(function () {
        $('#error_tutor_course').fadeOut(2000);
    });


    $('#btn_add').click(function (e) {
        if ($('#id_name_course').val() === "")
        {
            e.preventDefault();
            $('#error_name_course').fadeIn(1000);
        }
        else if ($("option:selected", '#id_subject').text() === "Не выбрано")
        {
            e.preventDefault();
            $('#error_subject_course').fadeIn(1000);
        }
        else if ($("option:selected", '#id_hotel').text() === "Не выбрано")
        {
            e.preventDefault();
            $('#error_tutor_course').fadeIn(1000)
        }
        else if ($('#id_information').val() === "")
        {
            e.preventDefault();
        }
    });


    $('#Entry').click(function (e) {
        e.preventDefault();
        var course_url = "/courses/" + $('#course_id').text() + "/";
        $.ajax({
            type: "POST",
            url: course_url,
            data: {csrfmiddlewaretoken: $('input[hotel_name=csrfmiddlewaretoken]').val()},
            success:function () {
                $('.course-obj-users').append($('#course_user').text());
                $('#Entry').css({"background-color": "gray", "box-shadow": "none"}).text("Вы уже записаны!").prop(
                    "disabled", true);
            }
        })
    })
});
