$(document).ready(function () {
  console.log($("#learn"))
  console.log($("#predict"))

  $("#learn-button").click(function (e) {
    console.log('click')
    e.preventDefault();
    $.ajax({
      type: "POST",
      url: "/model/learn",
      data: $(this).serialize(),
      success: function (response) {
        //alert("Response: " + response.status);
        alert("Модель успешно обучена");
        document.getElementById('learn-download').style.display = 'block'
        document.getElementById('predict').style.display = 'block'
      },
      error: function (error) {
        alert("Error: " + error.status);
      }
    });
  })

  $("#filtration").submit(function (e) {
    console.log('click')
    e.preventDefault();
    $.ajax({
      type: "POST",
      url: "/filtration",
      data: $(this).serialize(),
      success: function (response) {
        alert('Фильтрация');
        document.getElementById('filtration-download').href = "/download/" + response['filename'] + ".csv"
        document.getElementById('filtration-download').style.display = 'block'
      },
      error: function (error) {
        alert("Error: " + error.status);
      }
    });
  })

  $("#crosstab-form").submit(function (e) {
    let formData2 = new FormData(this);
    console.log('click')
    e.preventDefault();
    $.ajax({
      type: "POST",
      url: "/crosstab",
      data: formData2,
      dataType: "json",
      cache: false,
      processData: false,
      contentType: false,
      success: function (response) {
        alert("Пересчение таблиц");
        document.getElementById('crosstab-download').href = "/download/" + response['filename'] + ".csv"
        document.getElementById('crosstab-download').style.display = 'block'
      },
      error: function (error) {
        alert("Error: " + error.status);
      }
    });
  })

  console.log($("#common-plot-button"))
  $("#common-plot-button").click(function (e) {
    console.log($("#common-plot-select").val())
    $.ajax({
      url: '/plot/common/' + $("#common-plot-select").val(),
      type: 'GET',
      success: function (data) {
        plot = data['data']
        $("#common-plot-plot").html(plot);
      }
    });

  })

  $("#box-plot-button").click(function (e) {
    console.log($("#box-plot-select").val())
    $.ajax({
      url: '/plot/box/' + $("#box-plot-select-1").val() + "/" + $("#box-plot-select-2").val(),
      type: 'GET',
      success: function (data) {
        plot = data['data']
        $("#box-plot-plot").html(plot);
      }
    });

  })

  $("#scatter-plot-button").click(
    function () {
      console.log('change');
      $.ajax({
        url: '/plot/scatter/' +
          $("#scatter-plot-select-1").val() + "/" +
          $("#scatter-plot-select-2").val() + "/" +
          $("#scatter-plot-select-3").val() + "/" +
          $("#scatter-plot-select-4").val() + "/" +
          $("#scatter-plot-select-5").val()
        ,
        type: 'GET',
        success: function (data) {
          plot = data['data']
          $("#scatter-plot-plot").html(plot);
        }
      });
    });

  $("#pie-plot-button").click(
    function () {
      console.log('change');
      $.ajax({
        url: '/plot/pie/' +
          $("#pie-plot-select").val()
        ,
        type: 'GET',
        success: function (data) {
          plot = data['data']
          $("#pie-plot-plot").html(plot);
        }
      });
    });

  $("#learn-upload").submit(function (e) {
    console.log('click')
    e.preventDefault();
    let formData = new FormData(this);
    $.ajax({
      type: "POST",
      url: "/model/upload",
      data: formData,
      dataType: "json",
      cache: false,
      processData: false,
      contentType: false,
      success: function (response) {
        alert('Загрузка модели');
        document.getElementById('learn-download').style.display = 'block'
        document.getElementById('predict').style.display = 'block'
      },
      error: function (error) {
        alert("Error: " + error.status);
      }
    });
  })

  $("#predict-form").submit(function (e) {
    let formData = new FormData(this);
    console.log('click')
    e.preventDefault();
    $.ajax({
      type: "POST",
      url: "/model/predict",
      data: formData,
      dataType: "json",
      cache: false,
      processData: false,
      contentType: false,
      success: function (response) {
        alert("Вычисление значения");
        document.getElementById('predict_result').style.display = 'block'
        document.getElementById("predict_result-result").innerHTML = response['result'];
      },
      error: function (error) {
        alert("Error: " + error.status);
      }
    });
  })


document.getElementById("main-color").addEventListener("change", function() {
    document.body.style.backgroundColor = this.value;
});

document.getElementById("font-type").addEventListener("change", function() {
    document.body.style.fontFamily = this.value;
});

});

function showAddForm() {
  document.getElementById('add-form').style.display = 'block';
  document.getElementById('update-form').style.display = 'none';
  document.getElementById('delete-form').style.display = 'none';
}

// Отобразить форму для обновления записи
function showUpdateForm() {
  document.getElementById('add-form').style.display = 'none';
  document.getElementById('update-form').style.display = 'block';
  document.getElementById('delete-form').style.display = 'none';
}

// Отобразить форму для удаления записи
function showDeleteForm() {
  document.getElementById('add-form').style.display = 'none';
  document.getElementById('update-form').style.display = 'none';
  document.getElementById('delete-form').style.display = 'block';
}

// Обработчик события выбора radiobutton
document.querySelectorAll('input[type="radio"][name="radio-action"]').forEach(function (radio) {
  radio.addEventListener('click', function () {
    if (this.value === 'add') {
      showAddForm();
    } else if (this.value === 'update') {
      showUpdateForm();
    } else if (this.value === 'delete') {
      showDeleteForm();
    }
  });
});
