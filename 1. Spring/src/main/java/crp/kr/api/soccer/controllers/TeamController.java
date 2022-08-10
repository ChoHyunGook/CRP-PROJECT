package crp.kr.api.soccer.controllers;

import crp.kr.api.soccer.domains.Team;
import crp.kr.api.soccer.services.TeamService;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

/**
 * packageName:crp.kr.api.Soccer.controllers
 * fileName        :TeamController
 * author           : chohyungook
 * date               :2022-05-19
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-19chohyungook최초 생성
 */
@RestController
@RequiredArgsConstructor
@RequestMapping("/team")
public class TeamController {
    private final TeamService service;

    @GetMapping("/findAll")
    public List<Team> findAll() {
        return service.findAll();
    }

    @GetMapping("/findAll/sort")
    public List<Team> findAll(Sort sort) {
        return service.findAll(sort);
    }

    @GetMapping("/findAll/pageable")
    public Page<Team> findAll(Pageable pageable) {
        return service.findAll(pageable);
    }

    @GetMapping("/count")
    public long count() { return service.count(); }

    @DeleteMapping("/delete")
    public String delete(@RequestBody Team team) {
        return service.delete(team);
    }

    @PostMapping("/save")
    public String save(@RequestBody Team team) {
        return service.save(team);
    }

    @GetMapping("/findById/{teamNo}")
    public Optional<Team> findById(@PathVariable Long teamNo) { return service.findById(teamNo); }

    @GetMapping("/existsById/{teamNo}")
    public boolean existsById(@PathVariable Long teamNo) {  return service.existsById(teamNo); }
}
