import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { User } from './user.entity';
import { Repository } from 'typeorm';

@Injectable()
export class UsersService {
    constructor(@InjectRepository(User) private repo: Repository<User>) {} // Creamos la variable de tipo repositorio para usar la funciones del repositorio

    create(user: User) {
        return this.repo.save(user);
    }

    findAll() {
        return this.repo.find();
    }

    findOne(id: number) {
        return this.repo.findOneBy({id});
    }

    update(id: number, updatedUser: Partial<User>) { // Partial permite modificar los campos que quieran ser modificados, si solo es el nombre, solo el nombre se actualiza
        return this.repo.update(id, updatedUser);
    }

    delete(id: number) {
        return this.repo.delete(id);
    }
}
