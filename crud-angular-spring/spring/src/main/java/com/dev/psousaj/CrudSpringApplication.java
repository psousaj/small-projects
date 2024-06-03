package com.dev.psousaj;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import com.dev.psousaj.model.Course;
import com.dev.psousaj.repository.CourseRepository;

@SpringBootApplication
public class CrudSpringApplication {

	public static void main(String[] args) {
		SpringApplication.run(CrudSpringApplication.class, args);
	}

	@Bean
	CommandLineRunner initDataBase(CourseRepository repository) {
		return args -> {
			var course = new Course();
			course.setName("Inicio Servidor");
			course.setCategory("front-end");
			repository.save(course);

			// var course2 = new Course();
			// course.setName("Outro curso");
			// course.setCategory("front-end");
			// repository.save(course2);
		};
	}
}
