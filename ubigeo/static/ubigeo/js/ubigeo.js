function buildSelect(data) {
  return data.map(function (elem) {
    return '<option value="' + elem.id + '">' + elem.nombre + '</option>';
  }).join('');
}

function ubigeoSetup(baseUrl, departamentoSelector, provinciaSelector, distritoSelector) {
  var $dep = $(departamentoSelector);
  var $pro = $(provinciaSelector);
  var $dis = $(distritoSelector);

  var urls = {
    'provincias': baseUrl + 'provincias/',
    'distritos': baseUrl + 'distritos/',
  };

  $dep.on('change', function () {
    var selectedOption = $(this).find('option:selected').val();
    if (selectedOption.length) {
      var url = urls.provincias + '?departamento_id=' + selectedOption;
      $.getJSON(url, function (res) {
        $pro.html(buildSelect(res.data));
        $pro.trigger('change');
      });
    }
  });

  $pro.on('change', function () {
    var selectedOption = $(this).find('option:selected').val();
    if (selectedOption.length) {
      var url = urls.distritos + '?provincia_id=' + selectedOption;
      $.getJSON(url, function (res) {
        $dis.html(buildSelect(res.data));
      });
    }
  });
}
