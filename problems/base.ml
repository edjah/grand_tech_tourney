let func x =
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

    let lines = read_lines () in
    ()

let _ = main ()
