using UnityEngine;


public class Enemy2 : MonoBehaviour
{
    public float velocity = 4.0f;
    public int tipoMovimiento = 0;
    public Gun[] guns;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {


    }

    // Update is called once per frame
    void Update()
    {

    }
    private void FixedUpdate()
    {
        Vector2 pos = transform.position; //punto de origen del enemigo
        float moveAmount = velocity * Time.fixedDeltaTime; //cantidad de desplazamiento

        Vector2 move = Vector2.zero; //vector de movimiento


        if (tipoMovimiento == 0) //MRU
        {
            move.x -= moveAmount;
            move.y = 0;
        }
        if (tipoMovimiento == 1) //función definida a trozos
        {
            move.x -= moveAmount;
            float valor_x = pos.x + move.x; // coordenada X del punto al que llegamos
            if (valor_x < 6)
            {
                move.x -= moveAmount;
                move.y = 0;//no cambio en altura
            }
            else if (6 <= valor_x && valor_x < 9)
            {
                float valor_y = -(2 / 3f) * valor_x + 12; //coordenada Y del punto al que llegamos
                move.y = valor_y - pos.y; // cordenada en el eje Y del que voy a llegar - 
                move.x = -moveAmount; // valor_x -pos.x
            }
            else if (9 <= valor_x && valor_x < 12)
            {
                float valor_y = (2 / 3f) * valor_x + 0;
                move.y = valor_y - pos.y;
                move.x = -moveAmount;
            }
            else if (12 <= valor_x)
            {
                move.x -= moveAmount;
                move.y = 0;//no cambio en altura
            }
            pos += move; //punto+vector =punto
            transform.position = pos;

        }

        //





        if (pos.x < 0)
        {
            Destroy(gameObject);
        }
        //
        transform.position = pos;

    }
}
