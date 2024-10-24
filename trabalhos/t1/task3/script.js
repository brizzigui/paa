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

let matrix_of_solutions = [];
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

    matrix_of_solutions.push(tmp);
}

function merge_sort(arr, left, right) {
    if (left >= right)
        return;

    const mid = Math.floor(left + (right - left) / 2);
    merge_sort(arr, left, mid);
    merge_sort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}

function create_steps()
{
    let list = parse_array();

    merge_sort(list, 0, list.length-1);
    for (let i = 0; i < matrix_of_solutions.length; i++) {
        let line_pos_idx = Math.ceil(Math.log2(matrix_of_solutions[i].length));

        let string = `            
            <div class="container" id=""> ` +
            matrix_of_solutions[i] +
            `</div>`;
        document.getElementById("content").innerHTML += string;
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