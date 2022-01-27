
$('#getData').on('click', function() {
        $('#tb2').hide()
        $('#tb1').show()
        $('#tb3').hide()
        $.getJSON('http://apiapp.francecentral.azurecontainer.io/data_view/api/', function(data) {        
            for(var i in data) {
            var tr = document.createElement("tr")
            tr.setAttribute('class','trs')
                for(m in data[i])
                {
                    var td = document.createElement("td")
                    td.append(data[i][m])
                    td.setAttribute('class','tds pt-4')
                    tr.append(td)
                }
                var tbody = document.getElementById("tb")
                tbody.append(tr)
            }  
        });
    })
  
$('#getMean').on('click', function() {
        $('#tb1').hide()
        $('#tb2').show()
        $('#tb3').hide()
        $.getJSON('http://apiapp.francecentral.azurecontainer.io/data_view/api/means/', function(response) {        

            for(var i in response) {
                var tr = document.createElement("tr")
                tr.setAttribute('class','trs')
                for(m in response[i])
                {
                    var td = document.createElement("td")
                    td.append(response[i][m])
                    td.setAttribute('class','tds pt-4')
                    tr.append(td)
                }
        
                var tbody = document.getElementById("tbod")
                tbody.append(tr)
            }
        });
    })
$('#getStd').on('click', function() {
        $('#tb1').hide()
        $('#tb3').show()
        $('#tb2').hide()
        $.getJSON('http://apiapp.francecentral.azurecontainer.io/data_view/api/std/', function(resp) {        
            
            for(var i in resp) {
                var tr = document.createElement("tr")
                tr.setAttribute('class','trs')
                for(m in resp[i])
                {            
                    var td = document.createElement("td")
                    td.append(resp[i][m])           
                    td.setAttribute('class','tds pt-4')
                    tr.append(td)
                } 
                var tbody = document.getElementById("tbo")
                tbody.append(tr)
            }
        });
    })