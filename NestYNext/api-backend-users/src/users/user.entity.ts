import { Entity, PrimaryGeneratedColumn, Column } from "typeorm";

@Entity()
export class User {
    @PrimaryGeneratedColumn() // Indica que el atributo es primario y autoincrementador
    id: number;

    @Column() // Indica que son columnas
    name: string;

    @Column()
    email: string;
}