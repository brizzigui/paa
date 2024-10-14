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

function create_steps()
{
    console.log("called");
    let list = parse_array();
    for (let i = 0; i < Math.ceil(Math.log2(list.length)); i++) 
    {
         
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