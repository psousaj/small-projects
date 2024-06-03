package com.dev.psousaj.controller;

import java.util.List;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import com.dev.psousaj.model.Course;
import com.dev.psousaj.repository.CourseRepository;

import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;


@RestController
@RequestMapping("/api/courses")
@AllArgsConstructor
public class CoursesController {

    // @Autowired
    private final CourseRepository repository;

    // public CoursesController(CourseRepository courseRepository){
    //     this.repository = courseRepository;
    // }

    @GetMapping
    public List<Course> list(){
        return repository.findAll();
    }

    @PostMapping
    @ResponseStatus(code=HttpStatus.CREATED)
    public ResponseEntity<Course> cadastro(@RequestBody Course course) {
        var pessoa = repository.save(course);
        return ResponseEntity.ok(pessoa);
    }
    
}
