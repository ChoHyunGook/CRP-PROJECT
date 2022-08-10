package crp.kr.api.board.controllers;

import crp.kr.api.board.domains.Article;
import crp.kr.api.board.services.ArticleService;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

/**
 * packageName:crp.kr.api.board.controllers
 * fileName        :ArticleController
 * author           : chohyungook
 * date               :2022-05-09
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-09 chohyungook최초 생성
 */
@RestController
@RequiredArgsConstructor
@RequestMapping("/article")
public class ArticleController {
    private final ArticleService service;

    @GetMapping("/findAll")
    public List<Article> findAll() {
        return service.findAll();
    }

    @GetMapping("/findAll/sort")
    public List<Article> findAll(Sort sort) {
        return service.findAll(sort);
    }

    @GetMapping("/findAll/pageable")
    public Page<Article> findAll(Pageable pageable) {
        return service.findAll(pageable);
    }

    @GetMapping("/count")
    public long count() {
        return service.count();
    }

    @DeleteMapping("/delete")
    public String delete(@RequestBody Article article) {
        return service.delete(article);
    }

    @PostMapping("/save")
    public String save(@RequestBody Article article) {
        return service.save(article);
    }
}