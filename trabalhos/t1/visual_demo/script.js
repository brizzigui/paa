const WIDTH = 800;

function get_grid_num_children(id)
{
    return document.getElementById(id).childElementCount;
}

function set_columns_property(id)
{
    let string = "";
    let children = get_grid_num_children(id);

    for (let i = 0; i < children; i++) 
    {
        string += (WIDTH / children);
        string += "px ";      
    }

    document.getElementById(id).style.gridTemplateColumns = string;
}

let matrix_of_solutions = {};
function merge(arr, left, mid, right) {
    const n1 = mid - left + 1;
    const n2 = right - mid;

    // Create temp arrays
    const L = new Array(n1);
    const R = new Array(n2);

    // Copy data to temp arrays L[] and R[]
    for (let i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (let j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    let i = 0, j = 0;
    let k = left;

    let tmp = [];

    // Merge the temp arrays back into arr[left..right]
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }

        tmp.push(arr[k]);
        k++;
    }

    // Copy the remaining elements of L[], if there are any
    while (i < n1) {
        arr[k] = L[i];
        i++;
        tmp.push(arr[k]);
        k++;
    }

    // Copy the remaining elements of R[], if there are any
    while (j < n2) {
        arr[k] = R[j];
        j++;
        tmp.push(arr[k]);
        k++;
    }

}

let breaks = {};
let joins = {};

function symbolic_rejoin(cpy)
{
    let og = [];
    for (let i = 0; i < cpy.length; i++) {
        og.push([cpy[i]]);
    }

    let line = 0;
    do {  
        let aux = [];
        line += 1;
        for (let cur = 0; cur < og.length-1; cur+=2) {
            let tmp = [];
            let i = 0;
            let j = 0;
            let k = 0;
            // Merge the temp arrays back into arr[left..right]
            while (i < og[cur].length && j < og[cur+1].length) {
                if (og[cur][i] <= og[cur+1][j]) {
                    tmp[k] = og[cur][i];
                    i++;
                } else {
                    tmp[k] = og[cur+1][j];
                    j++;
                }

                k++;
            }

            // Copy the remaining elements of L[], if there are any
            while (i < og[cur].length) {
                tmp[k] = og[cur][i];
                i++;
                k++;
            }

            // Copy the remaining elements of R[], if there are any
            while (j < og[cur+1].length) {
                tmp[k] = og[cur+1][j];
                j++;
                k++;
            }

            aux.push([...tmp]);
        }

        if(og.length % 2 != 0)
            aux.push(og[og.length-1]);

        joins[line] = [...aux];
        og = [...aux];

    } while(og.length > 1)
}

function merge_sort(arr, left, right, rec_level) {

    if(breaks[rec_level] === undefined)
    {
        breaks[rec_level] = [];
        breaks[rec_level].push(arr.slice(left, right+1));
    }

    else
    {
        breaks[rec_level].push(arr.slice(left, right+1));
    }

    if (left >= right)
        return;

    const mid = Math.floor(left + (right - left) / 2);
    merge_sort(arr, left, mid, rec_level+1);
    merge_sort(arr, mid + 1, right, rec_level+1);
    merge(arr, left, mid, right);
}


function create_steps()
{
    let parent_div = document.getElementById("parent");
    parent_div.innerHTML = "";
    breaks = {};
    matrix_of_solutions = {};


    let list = parse_array();
    let cpy = [...list];
    merge_sort(list, 0, list.length-1, 0);


    for (let i = 0; i < 2*Math.ceil(Math.log2(list.length))+1; i++) {
        parent_div.innerHTML += '<div id="line_' + i + '"></div>';
    }

    let line_counter = 0
    for (const key in breaks) 
    {
        line_counter += 1;
        if(key == Math.ceil(Math.log2(list.length)))
        {
            cpy.forEach(element => {
                let values = '<div class="item">' + element + '</div>';
                let target = document.getElementById("line_"+key);
                target.innerHTML += '<div class="container">' + values + '</div>';
            })
            
            continue;
        }

        breaks[key].forEach(element => {
            let target = document.getElementById("line_"+key);
            let values = "";
            element.forEach(inner => {
                values += '<div class="item">' + inner + '</div>'
            })

            target.innerHTML += '<div class="container">' + values + '</div>';

        });
    }

    symbolic_rejoin(cpy);

    for (const key in joins) {
        joins[key].forEach(element => {
            let target = document.getElementById("line_"+(line_counter+parseInt(key)-1));
            let values = "";
            element.forEach(inner => {
                values += '<div class="item">' + inner + '</div>'
            })

            target.innerHTML += '<div class="container">' + values + '</div>';

        });
    }


}

function parse_array()
{
    let raw_string = document.getElementById("list_input").value;

    raw_string = raw_string.trim();
    raw_string = raw_string.replace("[", "");
    raw_string = raw_string.replace("]", "");
    raw_string = raw_string.replace("(", "");
    raw_string = raw_string.replace(")", "");

    let partial_list = [];
    if(raw_string.search(",") != -1)
    {
        partial_list = raw_string.split(",");
    }

    else
    {
        partial_list = raw_string.split(" ")
    }

    actual_list = [];
    for (let i = 0; i < partial_list.length; i++) {
        if(partial_list[i].length > 0 && !isNaN(partial_list[i]))
        {
            actual_list.push(parseInt(partial_list[i]));
        }
    }

    return actual_list;
}