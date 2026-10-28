using UnityEngine;
using UnityEngine.Assertions.Must;

public class Ship : MonoBehaviour
{
    public Gun[] guns;
    public float Speed;
    bool MoveUP;
    bool MoveDOWN;
    bool MoveLEFT;
    bool MoveRIGHT;
    bool SpeedUp;
    public float AumentoVelocidad = 2;
    bool shoot;

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        guns = GetComponentsInChildren<Gun>();
    }

    // Update is called once per frame
    void Update()
    {
        shoot = Input.GetKeyDown(KeyCode.L);
        MoveUP = Input.GetKey(KeyCode.W) || Input.GetKey(KeyCode.UpArrow);
        MoveDOWN = Input.GetKey(KeyCode.S) || Input.GetKey(KeyCode.DownArrow);
        MoveLEFT = Input.GetKey(KeyCode.A) || Input.GetKey(KeyCode.LeftArrow);
        MoveRIGHT = Input.GetKey(KeyCode.D) || Input.GetKey(KeyCode.RightArrow);
        SpeedUp = Input.GetKey(KeyCode.LeftShift);
        if (shoot)
        {
            shoot = false;
            foreach (Gun gun in guns)
            {
                gun.Shoot();
            }
        }
               
    }
    private void FixedUpdate()
    {
        Vector2 pos= transform.position; //punto
        float moveAmount = Speed * Time.fixedDeltaTime; //DISTANCIA = VELOCIDAD * TIEMPO
        Vector2 move = Vector2.zero;
        if (SpeedUp) {
            moveAmount *= AumentoVelocidad;
        }
        // Nos movemos
        if (MoveUP)
        {
            move.y += moveAmount;
        }
        if (MoveDOWN)
        {
            move.y -= moveAmount;
        }
        if (MoveLEFT)
        {
            move.x -= moveAmount;
        }
        if (MoveRIGHT)
        {
            move.x += moveAmount;
        }

        float moveMagnitude = Mathf.Sqrt(move.x * move.x + move.y * move.y); //Pitagoras nos permite conocer el tamaño del vector: lo que nos hemos movido
        if (moveMagnitude != moveAmount && moveMagnitude!=0) // si no me he movido lo que quería, corrijo
        {
            float ratio = moveAmount / moveMagnitude;
            move *= ratio;
        }



        pos += move; // punto inicial más vector de movimiento = punto final

        if (pos.x > 17) { pos.x = 17; }
        if (pos.x < 2) { pos.x = 2; }
        if (pos.y > 9.5f) { pos.y = 9.5f; }
        if (pos.y < 0.5f) { pos.y = 0.5f; }


        transform.position = pos;
    }
}
