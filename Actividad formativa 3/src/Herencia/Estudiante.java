
package Herencia;

public class Estudiante extends Persona{
    private int matricula;
    private float calificacion;
    
    //Constructor
    public Estudiante(String nombre,String apellido,int edad, int matricula, float calificacon){
    super(nombre,apellido,edad);
    this.matricula = matricula;
    this.calificacion = calificacion;
    }
    
    public void mostrarDatos(){
        System.out.println("Nombre: "+getNombre()+
                "\nApellido: "+getApellido()+
                "\nEdad: "+getEdad()+
                "\nmatricula; "+matricula+
                "\ncalificiacion; "+calificacion);
    }

}