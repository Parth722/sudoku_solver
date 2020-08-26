document.addEventListener('DOMContentLoaded', () => {
    
    function null_puzzle() {
        for(var i = 1; i <= 9; i++){
            var id = `#r${i}`;
            for(var j = 1; j <= 9; j++){
                document.querySelector(`${id} > #v${j} > input`).value = '';
                document.querySelector(`${id} > #v${j} > input`).style.color = 'black';
            }
        }  
    }
    null_puzzle();
    function is_empty(puzzle){
        for(var i = 0; i < 9; i++){
            for(var j = 0; j < 9; j++){
                if (puzzle[i][j] != '0'){
                    return false
                }
            }
        }
        return true
    }
    function create_puzzle() {
        var puzzle = [];
        for(var i = 1; i <= 9; i++){
            var id = `#r${i}`;
            var row = [];
            for(var j = 1; j <= 9; j++){
                var val = document.querySelector(`${id} > #v${j} > input`).value;
                if (val.length < 1){
                    row.push('0');
                }  
                else{
                    row.push(val);
                }   
            }
            puzzle.push(row);
        }
        return puzzle
        
    }

    function solved_puzzle(puzzle){
        for(var i = 1; i <= 9; i++){
            var id = `#r${i}`;
            for(var j = 1; j <= 9; j++){
                if (document.querySelector(`${id} > #v${j} > input`).value == 0){
                    document.querySelector(`${id} > #v${j} > input`).value = puzzle[i-1][j-1].toString();
                    document.querySelector(`${id} > #v${j} > input`).style.color = '#3944BC';
                } 

            }
        }
    }

    
    function solve(puzzle){
        $.ajax({
            type: "POST",
            data: {puzzle: JSON.stringify(puzzle)},
            url: "api/solve",
            success: function(msg){
                console.log(msg);
                solved_puzzle(msg)
            }
        })

    }
    var i = 0;
    var add_btn = document.querySelector('#add_btn');
    add_btn.addEventListener('click', () => {
        if (add_btn.innerHTML == 'Solve'){
            puzzle = create_puzzle();
            if (is_empty(puzzle)){
                alert('The Puzzle is empty, kindly add some values.')
            }else{
                solve(puzzle);
            }
        }
        if (i === 0){
            var reset = document.createElement('button');
            reset.classList.add('btn','btn-outline-dark');
            reset.innerHTML = 'Reset';
            reset.addEventListener('click', null_puzzle);
            document.getElementById('main').appendChild(reset)
            i += 1;
        }
        var puzzle_table = document.querySelector('#puzzle_table')
        puzzle_table.style.display = 'block';
        add_btn.innerHTML = 'Solve';
    }); 

})