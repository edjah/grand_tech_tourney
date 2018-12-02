let two_sum a target =
  failwith "TODO"


let main () =
    let read_lines () =
      let rec read_lines' res =
        try read_lines' (read_line () :: res)
        with End_of_file -> res
      in List.rev (read_lines' [])
    in

    let pop_last lst =
      let rec pop_last' orig new_lst =
        match orig with
        | [] -> failwith "pop on empty list"
        | [h] -> (h, List.rev new_lst)
        | h :: t -> pop_last' t (h :: new_lst)
      in pop_last' lst []
    in

    let numbers = List.map int_of_string (read_lines ()) in
    let numbers, search_value = pop_last numbers in
    let result = search numbers search_value in
    Printf.printf "%d\n" result

let _ = main ()
