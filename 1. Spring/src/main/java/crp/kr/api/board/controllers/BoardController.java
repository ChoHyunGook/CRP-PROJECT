package crp.kr.api.board.controllers;

import crp.kr.api.board.domains.Article;
import crp.kr.api.board.domains.Board;
import crp.kr.api.board.services.BoardService;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

/**
 * packageName:crp.kr.api.controllers
 * fileName        :BoardController
 * author           : chohyungook
 * date               :2022-05-04
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-04chohyungook최초 생성
 */
@RestController
@RequiredArgsConstructor
@RequestMapping("/board")
public class BoardController {
    private final BoardService service;

    @GetMapping("/findAll")
    public List<Board> findAll() {
        return service.findAll();
    }

    @GetMapping("/findAll/sort")
    public List<Board> findAll(Sort sort) {
        return service.findAll(sort);
    }

    @GetMapping("/findAll/pageable")
    public Page<Board> findAll(Pageable pageable) {
        return service.findAll(pageable);
    }

    @GetMapping("/count")
    public long count() {
        return service.count();
    }

    @DeleteMapping("/delete")
    public String delete(@RequestBody Board board) {
        return service.delete(board);
    }

    @PostMapping("/save")
    public String save(@RequestBody Board board) {
        return service.save(board);
    }

    @GetMapping("/findById/{id}")
    public Optional<Board> findById(@PathVariable String id) {
        return service.findById(id);
    }

    @GetMapping("/existsById/{id}")
    public boolean existsById(@PathVariable String id) {
        return service.existsById(id);
    }

}
