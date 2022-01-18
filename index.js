//JS Code link: https://doctorcodetutorial.blogspot.com/2019/08/search-filter-list-using-javascript.html?m=1

function filter() {
    var filterValue, input, ul, li, a, i;
    input = document.getElementById("search-input");
    filterValue = input.value.toUpperCase();
    ul = document.getElementById("search-list");
    a = ul.getElementsByTagName("a");


    for (i = 0; i < a.length; i++) {
      li = a[i].getElementsByTagName("li")[0];
      if (li.innerHTML.toUpperCase().indexOf(filterValue) > -1) {
            a[i].style.display = "";
        } 
      else {
            a[i].style.display = "none";
        }
    }
}

